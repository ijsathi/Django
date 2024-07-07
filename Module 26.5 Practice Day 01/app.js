document.addEventListener("DOMContentLoaded", () => {
    const apiUrl = "https://fakestoreapi.com/products";
    const spinner = document.getElementById('spinner');
    const noData = document.getElementById('no-data');
    const productList = document.getElementById("products");
    const categoryDropdown = document.getElementById("category-dropdown");

    const loadProducts = (category = "", search = "") => {
        productList.innerHTML = "";
        spinner.style.display = 'block';
        noData.style.display = 'none';

        let fetchUrl = apiUrl;
        if (category) {
            fetchUrl = `${apiUrl}/category/${category}`;
        } else if (search) {
            fetchUrl = `${apiUrl}?title_like=${search}`;
        }

        fetch(fetchUrl)
            .then((res) => res.json())
            .then((data) => {
                spinner.style.display = 'none';
                if (data.length > 0) {
                    noData.style.display = 'none';
                    displayProducts(data);
                } else {
                    productList.innerHTML = "";
                    noData.style.display = 'block';
                }
            })
            .catch((err) => {
                console.log(err);
                spinner.style.display = 'none';
                noData.style.display = 'block';
            });
    };

    const displayProducts = (products) => {
        products.forEach(product => {
            const parent = document.getElementById('products');
            const div = document.createElement('div');
            div.classList.add('col-md-3', 'product');
            div.innerHTML = `
                <div class="doc-card m-2">
                    <img src="${product.image}" alt="${product.title}">
                    <h3>${product.title.slice(0, 10)}...</h3>
                    <h6>$${product.price}</h6>
                    <p>${product.description.slice(0, 100)}...</p>
                    <a href="product-details.html?id=${product.id}" class="btn btn-primary">Details</a>
                </div>
            `;
            parent.appendChild(div);
        });
    };

    const loadCategory = () => {
        fetch('https://fakestoreapi.com/products/categories')
            .then((res) => res.json())
            .then((data) => {
                data.forEach((category) => {
                    const li = document.createElement('li');
                    li.classList.add('dropdown-item');
                    li.innerHTML = `<a class="nav-link" href="#" onclick="loadProducts('${category}')">${category}</a>`;
                    categoryDropdown.appendChild(li);
                });
            })
            .catch((err) => console.log(err));
    };

    window.showProductDetails = (productId) => {
        window.location.href = `product-details.html?id=${productId}`;
    };

    window.handleSearch = (event) => {
        event.preventDefault();
        const searchInput = document.getElementById('search-input').value;
        loadProducts("", searchInput);
    };

    loadCategory();
    loadProducts();
});
