import React from 'react';
import BlinkComparator from './components/BlinkComparator';

function App() {
  return (
    <div style={{ backgroundColor: '#0b0f19', minHeight: '100vh', color: '#fff', padding: '20px' }}>
      <header style={{ textAlign: 'center', marginBottom: '20px' }}>
        <h1 style={{ margin: 0, fontSize: '2rem', color: '#38bdf8' }}>NASA Space Data Blink Comparator</h1>
        <p style={{ color: '#94a3b8', fontSize: '0.95rem' }}>Comparing multi-epoch sky surveys to detect moving objects and transients</p>
      </header>
      <BlinkComparator />
    </div>
  );
}

export default App;