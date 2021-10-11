To do:
https://www.slickcharts.com/sp500

- Enable sorting: https://www.w3schools.com/howto/howto_js_sort_table.asp (funktioniert, ist aber extrem langsam)

- market weighting:
  - a = remaining weight
  - ∑a = sum of all remaining weights
  - b = scaling factor
  - **b = 100/∑a**
  - a' = a*b

**Next steps**
- add another column next to weight in % with the current weight of each stock that is checked
- calculate minimum investment in realtime 
- display number of positions, minimum investment in realtime

- return to flask: key-value pair of symbol and scaled weight: https://stackoverflow.com/questions/58109941/how-to-return-list-of-values-selected-in-dropdown-using-flask-and-html
- rewrite main.py to accept key:value pair instead of json


filter by industry: https://en.wikipedia.org/wiki/List_of_S%26P_500_companies

**minimum investment**
