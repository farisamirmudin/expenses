$host.ui.rawui.windowtitle = "Record Expenses"
$date = get-date
$csvfile = '{0}.csv' -f $date.date.month
$run = 'y'
while ($run -eq 'y') {
    clear-host
    $ask = $true
    do {
        $value = $(write-host 'Enter expenses: ' -foregroundcolor darkmagenta -nonewline; read-host).replace(',', '.')
        if ($value -match '[a-zA-Z\s]') {write-host 'Invalid Input. Restarting...'; clear-variable -name 'value'}
        else {$ask = $false}
    } while ($ask)
    
    $desc = $(write-host 'Enter description: ' -foregroundcolor green -nonewline; read-host)
    $content = [PSCustomObject]@{Date = get-date; Value = $value; Description = $desc}
    if (!(test-path -path $csvfile)) {
        $content | export-csv -path $csvfile
    } else {
        $content | export-csv -path $csvfile -append
    }
    clear-variable -name 'content'
    $run = (read-host -prompt 'Enter more [y/n]? ').tolower()
    if ($run -eq 'n') {
        write-host 'Closing...'
        start-sleep 0.5
    }
}