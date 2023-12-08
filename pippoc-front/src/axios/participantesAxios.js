import axios from "axios"

export const getParticipantes = () => {
    return axios
        .get('http://127.0.0.1:8000/participantes/')
        .then(response => {
            return response.data;
        })
        .catch(error => {
            console.error('Error getting participantes:', error);
            throw error;
        });
}

export const createParticipante = (participanteData) => {
    return axios.post('http://127.0.0.1:8000/participantes/', participanteData)
        .then(response => {
            return response.data;
        })
        .catch(error => {
            console.error('Error creating participante:', error);
            throw error;
        });
}