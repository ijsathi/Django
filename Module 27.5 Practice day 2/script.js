document.addEventListener('DOMContentLoaded', function() {
    const addUserForm = document.getElementById('add-user-form');
    if (addUserForm) {
        addUserForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const userData = {
                email: document.getElementById('email').value,
                username: document.getElementById('username').value,
                password: document.getElementById('password').value,
                name: {
                    firstname: document.getElementById('firstname').value,
                    lastname: document.getElementById('lastname').value
                },
                address: {
                    city: document.getElementById('city').value,
                    street: document.getElementById('street').value,
                    number: parseInt(document.getElementById('number').value, 10),
                    zipcode: document.getElementById('zipcode').value,
                    geolocation: {
                        lat: document.getElementById('lat').value,
                        long: document.getElementById('long').value
                    }
                },
                phone: document.getElementById('phone').value
            };

            fetch('https://fakestoreapi.com/users', {
                method: 'POST',
                body: JSON.stringify(userData),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('response').innerHTML = `<div class="alert alert-success">User added successfully!</div>`;
                addUserForm.reset();
                // Redirect to index.html after successful addition (optional)
                setTimeout(() => {
                    window.location.href = 'index.html';
                }, 1500); // Redirect after 1.5 seconds
            })
            .catch(error => console.error('Error:', error));
        });
    }

    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const loginData = {
                username: document.getElementById('login-username').value,
                password: document.getElementById('login-password').value
            };

            fetch('https://fakestoreapi.com/auth/login', {
                method: 'POST',
                body: JSON.stringify(loginData),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('response').innerHTML = `<div class="alert alert-success">User logged in successfully!</div>`;
                loginForm.reset();
                // Redirect to index.html after successful login (optional)
                setTimeout(() => {
                    window.location.href = 'index.html';
                }, 1500); // Redirect after 1.5 seconds
            })
            .catch(error => console.error('Error:', error));
        });
    }

    // Function to fetch all users and display them on index.html
    if (document.getElementById('response')) {
        getAllUsers();
    }
});

function getAllUsers() {
    fetch('https://fakestoreapi.com/users')
        .then(response => response.json())
        .then(data => {
            const responseDiv = document.getElementById('response');
            responseDiv.innerHTML = '';
            data.forEach(user => {
                const userCard = document.createElement('div');
                userCard.className = 'col-md-4 mb-3';
                userCard.innerHTML = `
                    <div class="card" onclick="window.location.href='user-details.html?id=${user.id}'">
                        <div class="card-body">
                            <h5 class="card-title">${user.name.firstname} ${user.name.lastname}</h5>
                            <p class="card-text">${user.email}</p>
                        </div>
                    </div>
                `;
                responseDiv.appendChild(userCard);
            });
        })
        .catch(error => console.error('Error:', error));
}
