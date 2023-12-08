import axios from "axios";

export const getDocumentos = () => {
    return axios
        .get('http://127.0.0.1:8000/documentos/')
        .then(response => {
            return response.data;
        })
        .catch(error => {
            console.error('Error getting documentos:', error);
            throw error;
        });
}