document.addEventListener("DOMContentLoaded", () => {
    const apiUrl = "https://fakestoreapi.com/products";
    const params = new URLSearchParams(window.location.search);
    const productId = params.get('id');

    const loadProductDetails = (id) => {
        fetch(`${apiUrl}/${id}`)
            .then((res) => res.json())
            .then((product) => displayProductDetails(product))
            .catch((err) => console.log(err));
    };

    const displayProductDetails = (product) => {
        const parent = document.getElementById('product-details');
        const div = document.createElement('div');
        div.classList.add('row');
        div.innerHTML = `
            <div class="col-md-6">
                <img src="${product.image}" alt="${product.title}" class="img-fluid">
            </div>
            <div class="col-md-6">
                <h2>${product.title}</h2>
                <p class="btn btn-success">${product.category}</p>
                <p>${product.description}</p>
                <p>Rating: ${product.rating.rate} out of 5 (${product.rating.count} reviews)</p>
                <h4>Price: ${product.price}$</h4>
            </div>
        `;
        parent.appendChild(div);
    };

    loadProductDetails(productId);
});
