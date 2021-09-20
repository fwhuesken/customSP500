const sectors = ["Industrials", "Health Care", "Information Technology", "Communication Services", "Consumer Staples", "Consumer Discretionary", "Utilities", "Financials", "Materials", "Real Estate", "Energy"]

const sectorDropDown = document.getElementById('sector-experiment')


//Populate dropdown menus
sectorDropDown.innerHTML = sectors.map(player => `<option value="${sectors}">${sectors}</option>`).join(''));