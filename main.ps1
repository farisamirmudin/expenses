$host.ui.rawui.windowtitle = "Record Expenses"
$date = get-date
$csvfile = '{0}.csv' -f $date.date.month
$run = 'y'
while ($run -eq 'y') {
    clear-host
    $value = $(write-host 'Enter expenses: ' -foregroundcolor darkmagenta -nonewline; read-host).replace(',', '.')
    $desc = $(write-host 'Enter description: ' -foregroundcolor green -nonewline; read-host)
    $content = [PSCustomObject]@{Date = get-date; Value = $value; Description = $desc}
    if (!(test-path -path $csvfile)) {
        $content | export-csv -path $csvfile
    } else {
        $content | export-csv -path $csvfile -append
    }
    clear-variable -name 'content'
    $run = read-host -prompt 'Enter more [y/n]? '
    write-host 'Closing...'
    start-sleep 1.0
}