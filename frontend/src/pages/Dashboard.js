import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PerformanceChart from '../components/Dashboard/PerformanceChart';

const Dashboard = () => {
  const [performances, setPerformances] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/performance/')
      .then(response => setPerformances(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Desempenho dos Alunos</h1>
      <PerformanceChart data={performances} />
      <ul>
        {performances.map(performance => (
          <li key={performance.id}>
            {performance.student_id} - {performance.topic}: {performance.score}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;
