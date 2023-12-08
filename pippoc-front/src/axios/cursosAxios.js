import axios from 'axios'

export const createCurso = (cursoData) => {
    return axios.post('http://127.0.0.1:8000/cursos/', cursoData)
      .then(response => {
        return response.data;
      })
      .catch(error => {
        console.error('Error creating curso:', error);
        throw error;
      });
  };

export const getCursos = () => {
    return axios.get('http://127.0.0.1:8000/cursos/')
        .then(response => {
            return response.data;
        })
        .catch(error => {
            console.error('Error getting cursos:', error);
            throw error;
        });
}