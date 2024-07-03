const loadServices = ()=>{
    fetch('https://testing-8az5.onrender.com/services/')
    .then((res)=>res.json())
    .then((data)=>displayServices(data))
    .catch((err)=>console.log(err))
};
const displayServices = (services)=>{
    services.forEach(service => {
        const parent = document.getElementById('service-container');
        const li = document.createElement('li');
        li.innerHTML = `
            <div class="card shadow h-100">
                <div class="ratio ratio-16x9">
                    <img src=${service.image} class="card-img-top" loading="lazy" alt="...">
                </div>
                <div class="card-body  p-4">
                    <h3 class="card-title h5">${service.name}</h3>
                    <p class="card-text">${service.description.slice(0, 130)}...</p>
                    <a href="#" class="btn btn-primary">Details</a>
                </div>
            </div>
        `
    parent.appendChild(li);
    });
};

// for slider active

loadServices();