<template>
  <div>
    <h2>List of Courses</h2>
    <ul>
      <li v-for="curso in cursos" :key="curso.id">
        {{ curso.descripcion }} - {{ curso.categoria }}
      </li>
    </ul>
    <h2>List of Participantes</h2>
    <ul>
      <li v-for="participante in participantes" :key="participante.id">
        {{ participante.nombre }} - {{ participante.apellido }} - {{ participante.correo }}
      </li>
    </ul>
  </div>
</template>

<script>
import { getCursos } from '../axios/cursosAxios';
import { getParticipantes } from '../axios/participantesAxios';

export default {
  data() {
    return {
      cursos: [],
      participantes: [],
    };
  },
  mounted() {
    // Fetch cursos from Django backend using the imported function
    getCursos()
      .then(data => {
        this.cursos = data;
        // After fetching cursos, fetch participantes
        return getParticipantes();
      })
      .then(data => {
        this.participantes = data;
      })
      .catch(error => {
        // Handle error if needed
      });
  },
  // Other methods and component logic
};
</script>
