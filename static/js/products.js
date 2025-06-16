document.addEventListener('DOMContentLoaded', function() {
    const token = localStorage.getItem("access_token");

    if (!token) {
        alert("You are not logged in.");
        window.location.href = "/";
        return;
    }

    const tbody = document.querySelector('.products-table tbody');
    const searchInput = document.getElementById('search-input');
    const searchBtn = document.getElementById('search-button');
    const modal = document.getElementById('product-modal');
    const modalContent = document.getElementById('modal-product-details');
    const closeBtn = document.querySelector('.modal-close');

    // Fetch products from API
    fetch("/products", {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`
        }
    })
    .then(res => {
        if (!res.ok) throw new Error("Failed to fetch products");
        return res.json();
    })
    .then(products => {
        products.forEach(p => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${p.id}</td>
                <td>${p.name}</td>
                <td>${p.description}</td>
                <td>$${p.price.toFixed(2)}</td>
                <td>
                    <button class="view-button" data-id="${p.id}" aria-label="View ${p.name}">
                        <i class="fas fa-eye"></i>
                    </button>
                    <button class="edit-button" data-id="${p.id}" aria-label="Edit ${p.name}">
                        <i class="fas fa-edit"></i>
                    </button>
                </td>
            `;
            tbody.appendChild(row);
        });

        attachEventListeners(); // Hook buttons after DOM is ready
    })
    .catch(err => {
        console.error(err);
        alert("Session expired or unauthorized. Please log in again.");
        window.location.href = "/";
    });

    function attachEventListeners() {
        const tableRows = document.querySelectorAll('.products-table tbody tr');

        // Search
        function performSearch() {
            const searchTerm = searchInput.value.toLowerCase();
            tableRows.forEach(row => {
                const name = row.children[1].textContent.toLowerCase();
                const desc = row.children[2].textContent.toLowerCase();
                row.style.display = name.includes(searchTerm) || desc.includes(searchTerm) ? '' : 'none';
            });
        }

        searchBtn.addEventListener('click', performSearch);
        searchInput.addEventListener('keyup', e => {
            if (e.key === "Enter") performSearch();
        });

        // View
        document.querySelectorAll('.view-button').forEach(button => {
            button.addEventListener('click', function() {
                const row = this.closest('tr');
                const name = row.children[1].textContent;
                const description = row.children[2].textContent;
                const price = row.children[3].textContent;
                modalContent.innerHTML = `
                    <h2>${name}</h2>
                    <p><strong>Description:</strong> ${description}</p>
                    <p><strong>Price:</strong> ${price}</p>
                `;
                modal.style.display = 'block';
            });
        });

        closeBtn.addEventListener('click', () => modal.style.display = 'none');
        window.addEventListener('click', e => {
            if (e.target === modal) modal.style.display = 'none';
        });

        // Edit
        document.querySelectorAll('.edit-button').forEach(button => {
            button.addEventListener('click', function() {
                const productId = this.getAttribute('data-id');
                alert(`Edit product ${productId} (implement your logic here)`);
            });
        });
    }
});

