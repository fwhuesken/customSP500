To do:

**~~Weighting~~**
- ~~Create json file from csv in selection.py (makes it easier when I later generate json in JS) which includes weights~~
- ~~rewrite final_selection() to work with json file~~
- ~~rewrite buy() to work with new final_selection()~~
- ~~Check if weights and minimum price work in buying power check~~

**~~GUI~~**
- ~~List all fractionable shares
**=> Use PTL approach to get data from database, then use replit approach to display it**~~

- ~~add sp500~~~
- ~~add nasdaq100~~~
- ~~add dropdown to select different indexes~~~
- ~~display selected data~~
- ~~separate table for sector needed~~
- ~~let user select which ones to drop~~
- ~~figure out how the filter function works and apply to sector dropdown~~
- ~~add button that removes all checks~~
- add weighting button that removes all unchecked companies and displays selection option
- on that next page, show selection and allow weighting (market cap and equal)
- OR: remove all non-necessary elements /  all checked stocks from DOM and display submit button / weighting option
- ~~onLoad: all fractionable equities are displayed~~
- HTML table to json: https://stackoverflow.com/questions/6271856/html-table-to-json
- allow users to download selection as .csv (and upload it)
**Generally: How come baselineIndex, countPositions don't work? addEventListener better to manipulate DOM?**

**Misc**
- Assign weights (% and $)
- Show minimum per month with current selection
- change sp500.py so it accepts all csv (make sure to assign table name based on csv name)
- display multi dropdown on index.html to join tables
- config: same file in two places
- automate dropdowns by launching script.js (doesn't work so far with flask), see manual.txt in static folder
- rewrite main.py so that index dropdown value determines database pull without additional if statements for new baseline indexes


**ETF**
- Store ETF composition in table
- Calculate current overall price for ETF (and change)
- need sector data for all fractionable stocks
- use JOIN to display constituents of sp500 and nasdaq together