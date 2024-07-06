const getParams = () => {
    const param = new URLSearchParams(window.location.search).get('doctorId');
    fetch(`https://testing-8az5.onrender.com/doctor/list/${param}`)
        .then(res => res.json())
        .then(data => displayDetails(data))
        .catch(error => console.error('Error fetching doctor details:', error));

    fetch(`https://testing-8az5.onrender.com/doctor/review/?doctor_id=${param}`)
        .then(res => res.json())
        .then(data => docReview(data))
        .catch(error => console.error('Error fetching review details:', error));
}

const displayDetails = (detail) => {
    // console.log(detail);
    const parent = document.getElementById('doctor-details');
    const div = document.createElement('div');
    div.innerHTML = `
        <div class="doctor-details">
            <div class="doc-img">
                <img src=${detail.image} alt="">
            </div>
            <div class="doc-info w-50 m-auto">
                <h3>${detail.full_name}</h3>
                <p class="fw-bold">${detail.designation}</p>
                <p><small>${detail?.specialization?.map((item) => {
        return `${item}`
    })}</small> </p>
                <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quibusdam vitae harum, saepe nostrum distinctio maiores officiis ab doloribus molestiae, illum ea soluta impedit cum optio suscipit, tempore aut mollitia placeat.</p>
                <h5>Fees: ${detail.fee}</h5>
                <a href="" class="btn btn-success">Take Appointment</a>
            </div>
        </div>
        `;
    parent.appendChild(div);
};

const docReview = (review) => {
    const parent = document.getElementById('doc-details-review');
    const li = document.createElement('li');
        // Format the review date
    // const formattedDate = new Date(review.created_on).toLocaleDateString('en-US', {
    //     timeZone: "Asia/Dhaka",
    //     year: 'numeric',
    //     month: 'short',
    //     day: 'numeric',
    //     hour: 'numeric',
    //     minute: 'numeric',
    //     hour12: true
    // });

    li.innerHTML = `
        <li class="review-card">
            <img src="../images/blank-img.jpg" alt="">
            <h4>${review.reviewer}</h4>
            <p>${review.body}</p>
            <p>${review.rating}</p>
            <p>For ${review.doctor}</p>
        </li>
        `
    parent.appendChild(li);
}

getParams();