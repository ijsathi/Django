const loadServices = () => {
    fetch('https://testing-8az5.onrender.com/services/')
        .then((res) => res.json())
        .then((data) => displayServices(data))
        .catch((err) => console.log(err))
};
const displayServices = (services) => {
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

const loadDoctors = (search) => {
    document.getElementById('doctors').innerHTML = "";
    document.getElementById('spinner').style.display = 'block';
    fetch(`https://testing-8az5.onrender.com/doctor/list/?search=${search ? search : ""}`)
        .then((res) => res.json())
        .then((data) => {
            if (data.results.length > 0) {
                document.getElementById('spinner').style.display = 'none';
                document.getElementById('no-data').style.display = 'none';
                displayDoctors(data?.results);
            }
            else {
                document.getElementById('doctors').innerHTML = "";
                document.getElementById('spinner').style.display = 'none';
                document.getElementById('no-data').style.display = 'block';
            }
        })
        .catch((err) => console.log(err))
};
const displayDoctors = (doctors) => {
    doctors?.forEach(doctor => {
        const parent = document.getElementById('doctors');
        const div = document.createElement('div');
        div.innerHTML = `
            <div class="doc-card m-2">
                <img src=${doctor?.image} alt="">
                <h3>${doctor?.full_name}</h3>
                <h6>${doctor.designation} </h6>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque, assumenda.</p>
                <p><small>${doctor?.specialization?.map((item) => {
            return `<button class='btn btn-warning'>${item}</button>`
        })}</small> </p>
                <a href="../doctors/doc-details.html?doctorId=${doctor.id}" class="btn btn-primary">Details</a>
            </div>
        `
        parent.appendChild(div);
    });
}

const loadDesignation = () => {
    fetch('https://testing-8az5.onrender.com/doctor/designation/')
        .then((res) => res.json())
        .then((data) => {
            data.forEach((item) => {
                const parent = document.getElementById("designation-dropdown");
                const li = document.createElement('li');
                li.classList.add('dropdown-item');
                li.innerHTML = `
                <li onclick="loadDoctors('${item?.name}')">${item?.name}</li>
                `
                parent.appendChild(li)
            });
        })
        .catch((err) => console.log(err))
};

const loadSpecialization = () => {
    fetch('https://testing-8az5.onrender.com/doctor/specialization/')
        .then((res) => res.json())
        .then((data) => {
            data.forEach((item) => {
                const parent = document.getElementById("specialization-dropdown");
                const li = document.createElement('li');
                li.classList.add('dropdown-item');
                li.innerHTML = `
            <li onclick="loadDoctors('${item?.name}')">${item?.name}</li>
            `;
                parent.appendChild(li)
            });
        })
        .catch((err) => console.log(err))
};

const handleSearch = () => {
    const value = document.getElementById('search').value;
    loadDoctors(value)
};

const loadReviews = () => {
    fetch('https://testing-8az5.onrender.com/doctor/review/')
        .then((res) => res.json())
        .then((data) => displayReviews(data))
        .catch((err) => console.log(err))
};
const displayReviews = (reviews) => {
    reviews.forEach(review => {
        const parent = document.getElementById('review-container');
        const li = document.createElement('li');
        // Format the review date
        const formattedDate = new Date(review.created_on).toLocaleDateString('en-US', {
            timeZone: "Asia/Dhaka",
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: 'numeric',
            minute: 'numeric',
            hour12: true
        });

        li.innerHTML = `
            <div class="review-card">
                <img src="../images/blank-img.jpg" alt="">
                <h4>${review.reviewer}</h4>
                <p>${review.body.slice(0,150)}</p>
                <p>${review.rating}</p>
                <p>For ${review.doctor}</p>
                <p>${formattedDate}</p>
            </div>
        `
        parent.appendChild(li);
    });
};

loadReviews();
loadSpecialization();
loadDesignation();
loadDoctors();
loadServices();