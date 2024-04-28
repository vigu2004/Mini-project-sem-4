function predict() {
    const fileInput = document.getElementById('fileInput');
    const predictionResult = document.getElementById('predictionResult');
    const file = fileInput.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('image', file);

        fetch('/predict', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                predictionResult.innerHTML = `<p>Prediction: ${data.prediction}</p>`;
            })
            .catch(error => {
                console.error('Error:', error);
                predictionResult.innerHTML = '<p>Error occurred during prediction. Please try again.</p>';
            });
    } else {
        predictionResult.innerHTML = '<p>No file selected.</p>';
    }
}
