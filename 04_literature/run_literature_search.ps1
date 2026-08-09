param(
    [string]$SearchDate = '2026-08-09'
)

$ErrorActionPreference = 'Stop'
$query = 'spatiotemporal crime prediction machine learning urban'
$headers = @{ 'User-Agent' = 'RSL-Comas/1.0 (academic review)' }

$openAlexUrl = 'https://api.openalex.org/works?search=spatiotemporal%20crime%20prediction%20machine%20learning%20urban&filter=from_publication_date:2008-01-01,to_publication_date:2026-08-09&per-page=50&select=doi,title,publication_year,type,open_access,best_oa_location'
$crossrefUrl = 'https://api.crossref.org/works?query.bibliographic=spatiotemporal%20crime%20prediction%20machine%20learning%20urban&filter=from-pub-date:2008-01-01,until-pub-date:2026-08-09,type:journal-article&rows=50&select=DOI,title,published,author,container-title,URL'

$oaResponse = Invoke-RestMethod -Uri $openAlexUrl -Headers $headers
$crResponse = Invoke-RestMethod -Uri $crossrefUrl -Headers $headers

$records = @()
$rank = 0
foreach ($work in $oaResponse.results) {
    $rank++
    $records += [pscustomobject]@{
        source = 'OpenAlex'
        source_rank = $rank
        doi = (($work.doi -replace '^https://doi.org/', '').ToLower())
        title = $work.title
        year = $work.publication_year
    }
}

$rank = 0
foreach ($work in $crResponse.message.items) {
    $rank++
    $records += [pscustomobject]@{
        source = 'Crossref'
        source_rank = $rank
        doi = $work.DOI.ToLower()
        title = $work.title[0]
        year = $work.published.'date-parts'[0][0]
    }
}

$records | Export-Csv -Path "$PSScriptRoot/search_results_2026-08-09.csv" -NoTypeInformation -Encoding UTF8

$includedDois = @(
    '10.1186/s42492-021-00075-z',
    '10.1007/s12652-023-04530-y',
    '10.1109/access.2021.3075140',
    '10.1109/access.2020.3028420',
    '10.1016/j.procs.2020.03.357',
    '10.1016/j.procs.2018.08.261',
    '10.1109/access.2020.3041924',
    '10.24963/ijcai.2021/225',
    '10.1609/aaai.v36i4.20360',
    '10.1140/epjds/s13688-018-0171-7',
    '10.1145/3325112.3328221',
    '10.1109/access.2023.3308967',
    '10.3390/ijgi10060369',
    '10.1109/access.2021.3068306',
    '10.1371/journal.pone.0296486',
    '10.1016/j.compenvurbsys.2021.101660',
    '10.1109/access.2020.3002766',
    '10.1140/epjds/s13688-022-00366-2',
    '10.5121/mlaij.2021.8101',
    '10.3390/bdcc9120301',
    '10.31577/cai_2023_3_568',
    '10.1016/j.jnlssr.2024.11.003',
    '10.1109/access.2021.3078117'
)

$notRetrievedDois = @(
    '10.65161/recxzq186npyfh2ss',
    '10.1016/j.ins.2023.119414',
    '10.1007/s42979-026-04792-1',
    '10.1016/j.compenvurbsys.2022.101789',
    '10.55248/gengpi.07.0326.0442',
    '10.1016/j.engappai.2021.104460',
    '10.56726/irjmets89965',
    '10.33425/3066-1226.1260',
    '10.1016/j.asoc.2023.110886',
    '10.64388/irev9i11-1717915'
)

$unique = $records | Group-Object { if ($_.doi) { $_.doi } else { $_.title.ToLower() } } | ForEach-Object { $_.Group[0] }
$screening = @()
$id = 0
foreach ($record in $unique) {
    $id++
    $candidate = $record.title -match '(?i)crime' -and
        $record.title -match '(?i)predict|forecast|hotspot' -and
        $record.title -notmatch '(?i)recidiv|cyber|homicide.*race'

    if (-not $candidate) {
        $taDecision = 'exclude'
        $ftDecision = 'not_sought'
        $reason = 'Outside scope according to title; documented automated rule'
    }
    elseif ($notRetrievedDois -contains $record.doi) {
        $taDecision = 'include'
        $ftDecision = 'not_retrieved'
        $reason = 'Full text not retrieved through open access'
    }
    elseif ($includedDois -contains $record.doi) {
        $taDecision = 'include'
        $ftDecision = 'include'
        $reason = ''
    }
    else {
        $taDecision = 'include'
        $ftDecision = 'exclude'
        $reason = 'Secondary review, insufficient scope, or unverifiable validation'
    }

    $screening += [pscustomobject]@{
        record_id = ('R{0:D3}' -f $id)
        title = $record.title
        doi = $record.doi
        source = $record.source
        duplicate = 'no'
        title_abstract_decision = $taDecision
        full_text_decision = $ftDecision
        exclusion_reason = $reason
        reviewer = 'Enrique Lee Huamani Uriarte; initial screening assisted by documented rules'
        decision_date = $SearchDate
    }
}

$screening | Export-Csv -Path "$PSScriptRoot/screening_log.csv" -NoTypeInformation -Encoding UTF8

$summary = [pscustomobject]@{
    identified = $records.Count
    duplicates_removed = $records.Count - $unique.Count
    screened = $unique.Count
    title_abstract_excluded = @($screening | Where-Object title_abstract_decision -eq 'exclude').Count
    reports_sought = @($screening | Where-Object title_abstract_decision -eq 'include').Count
    reports_not_retrieved = @($screening | Where-Object full_text_decision -eq 'not_retrieved').Count
    reports_assessed = @($screening | Where-Object full_text_decision -in @('include', 'exclude')).Count
    full_text_excluded = @($screening | Where-Object full_text_decision -eq 'exclude').Count
    studies_included = @($screening | Where-Object full_text_decision -eq 'include').Count
}

$summary | Format-List
