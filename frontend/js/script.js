/**
 * Simple Investment Management - Frontend Logic
 * Handles interactive dashboard actions, modal popups, and financial metrics math.
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log("InvestManager UI Engine Initialized.");

    // Initialize core dashboard functionalities
    initNegativeMetricHighlighter();
    initTransactionModal();
    recalculatePortfolioSummary();
});

/**
 * 1. AUTOMATIC COLOR CORRECTION FOR LOSSES
 * Automatically checks table data cells or metrics. If a value starts with a minus '-',
 * it swaps the utility class from 'profit' to 'loss' so it turns red.
 */
function initNegativeMetricHighlighter() {
    const dynamicValues = document.querySelectorAll('.profit, .loss, .data-table td');
    
    dynamicValues.forEach(element => {
        const text = element.textContent.trim();
        if (text.startsWith('-')) {
            element.classList.remove('profit');
            element.classList.add('loss');
        } else if (text.startsWith('+')) {
            element.classList.remove('loss');
            element.classList.add('profit');
        }
    });
}

/**
 * 2. TRANSACTION MODAL CONTROLLER
 * Dynamically injects and manages the "+ Add Transaction" overlay popup.
 */
function initTransactionModal() {
    const addBtn = document.querySelector('.header-summary .btn');
    if (!addBtn) return;

    // Create Modal HTML structures programmatically
    const modal = document.createElement('div');
    modal.id = 'transactionModal';
    modal.style.cssText = `
        display: none; position: fixed; z-index: 1000; left: 0; top: 0;
        width: 100%; height: 100%; background-color: rgba(0,0,0,0.5);
        align-items: center; justify-content: center;
    `;

    modal.innerHTML = `
        <div class="auth-container" style="margin: 0; width: 90%; max-width: 450px; position: relative;">
            <span id="closeModal" style="position: absolute; right: 20px; top: 15px; cursor: pointer; font-size: 1.5rem; color: var(--text-secondary);">&times;</span>
            <div class="auth-header" style="margin-bottom: 15px;">
                <h3>Add New Transaction</h3>
            </div>
            <form id="transactionForm">
                <div class="form-group">
                    <label>Asset Name</label>
                    <input type="text" id="txName" class="form-control" placeholder="e.g., Microsoft" required>
                </div>
                <div class="form-group">
                    <label>Ticker Symbol</label>
                    <input type="text" id="txTicker" class="form-control" placeholder="e.g., MSFT" required>
                </div>
                <div class="form-group" style="display: flex; gap: 10px;">
                    <div style="flex: 1;">
                        <label>Shares</label>
                        <input type="number" step="any" id="txShares" class="form-control" placeholder="0" required>
                    </div>
                    <div style="flex: 1;">
                        <label>Price ($)</label>
                        <input type="number" step="any" id="txPrice" class="form-control" placeholder="0.00" required>
                    </div>
                </div>
                <button type="submit" class="btn">Log Transaction</button>
            </form>
        </div>
    `;

    document.body.appendChild(modal);

    // Event Listeners to Open/Close
    addBtn.addEventListener('click', () => modal.style.display = 'flex');
    
    modal.querySelector('#closeModal').addEventListener('click', () => modal.style.display = 'none');
    
    window.addEventListener('click', (e) => {
        if (e.target === modal) modal.style.display = 'none';
    });

    // Handle form logging submission
    const form = modal.querySelector('#transactionForm');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const name = document.getElementById('txName').value;
        const ticker = document.getElementById('txTicker').value.toUpperCase();
        const shares = parseFloat(document.getElementById('txShares').value);
        const price = parseFloat(document.getElementById('txPrice').value);
        
        addNewRowToHoldings(name, ticker, shares, price);
        
        // Reset form and dismiss
        form.reset();
        modal.style.display = 'none';
    });
}

/**
 * 3. DYNAMIC DOM APPENDING
 * Appends the logged asset transaction straight onto your HTML table container.
 */
function addNewRowToHoldings(name, ticker, shares, price) {
    const tableBody = document.querySelector('.data-table tbody');
    if (!tableBody) return;

    const currentVal = shares * price;
    const mockReturn = (Math.random() * 15 - 5).toFixed(1); // Generates standard mock yield variances

    const row = document.createElement('tr');
    row.innerHTML = `
        <td><strong>${name}</strong></td>
        <td>${ticker}</td>
        <td>${shares}</td>
        <td>$${price.toFixed(2)}</td>
        <td>$${currentVal.toFixed(2)}</td>
        <td class="${mockReturn >= 0 ? 'profit' : 'loss'}">${mockReturn >= 0 ? '+' : ''}${mockReturn}%</td>
    `;

    tableBody.appendChild(row);
    recalculatePortfolioSummary();
}

/**
 * 4. FINANCIAL SUMMARY MATHEMATICS
 * Parses values from the data table to calculate net portfolio values and investment holdings.
 */
function recalculatePortfolioSummary() {
    const rows = document.querySelectorAll('.data-table tbody tr');
    let totalValue = 0;

    rows.forEach(row => {
        const valueText = row.cells[4].textContent.replace(/[^0-9.-]/g, '');
        totalValue += parseFloat(valueText) || 0;
    });

    // Update the "Total Portfolio Value" top status card dynamically
    const summaryCards = document.querySelectorAll('.metrics-grid .card .value');
    if (summaryCards.length > 0) {
        summaryCards[0].textContent = `$${totalValue.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
    }
}
