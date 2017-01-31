set output 'AWS_write_latency.png'
set bar 1.000000 front
set boxwidth 0.2 relative
set style circle radius graph 0.02, first 0.00000, 0.00000
set style ellipse size graph 0.05, 0.03, first 0.00000 angle 0 units xy
set style textbox transparent margins  1.0,  1.0 border
set logscale x 2

unset paxis 1 tics
unset paxis 2 tics
unset paxis 3 tics
unset paxis 4 tics
unset paxis 5 tics
unset paxis 6 tics

set title "AWS write latency for various object sizes"
set xrange [ 8 : 4096 ] noreverse nowriteback
set yrange [ 0 : 5000 ] noreverse nowriteback
set colorbox vertical origin screen 0.9, 0.2, 0 size screen 0.05, 0.6, 0 front #noinvert bdefault
x = 0.0

## Last datafile plotted: "candlesticks.dat"
plot 'cstick.dat' using 1:3:2:6:5 with candlesticks lt 3 lw 2 title 'Boundaries of the box represent 1st and 3rd quartiles', '' using 1:4:4:4:4 with candlesticks lt -1 lw 2 notitle
pause -1
