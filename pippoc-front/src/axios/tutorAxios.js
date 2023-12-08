import axios from 'axios'

export const createTutor = (tutorData) => {
    return axios.post('http://http://127.0.0.1:8000/tutor/', tutorData)
        .then(response => {
            return response.data;
        })
        .catch(error => {
            console.error('Error creating tutor:', error);
            throw error;
        });
}

export const getTutores = () => {
    return axios.get('http://http://127.0.0.1:8000/tutor/')
        .then(response => {
            return response.data;
        })
        .catch(error => {
            console.error('Error getting tutor:', error);
            throw error;
        });
}

