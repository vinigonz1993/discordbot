import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import Main from './components/Main';
import Menu from './components/common/Menu';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import OCT from './components/OCT';
import Container from './components/common/Container';

function App() {
  return (
    <BrowserRouter>
      <Menu />
      <Container>
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/o" element={<OCT />} />
        </Routes>
      </Container>
    </BrowserRouter>
  )
}

export default App;
