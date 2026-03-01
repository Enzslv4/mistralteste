import React from 'react';
import { Bar } from 'react-chartjs-2';

const PerformanceChart = ({ data }) => {
  return <Bar data={data} />;
};

export default PerformanceChart;
