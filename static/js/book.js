const modal = document.getElementById('bookingModal');
const span = document.getElementsByClassName("close")[0];
const form = document.getElementById('appointmentForm');
const expertNameInput = document.getElementById('expertName');

function openModal(expertName) {
    modal.style.display = "block";
    expertNameInput.value = expertName;
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

form.addEventListener('submit', function(e) {
    e.preventDefault();
    const expert = expertNameInput.value;
    const date = document.getElementById('appointmentDate').value;
    const time = document.getElementById('appointmentTime').value;
    alert(`Appointment booked with ${expert} on ${date} at ${time}`);
    modal.style.display = "none";
});