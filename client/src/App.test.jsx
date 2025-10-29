// client/src/App.test.jsx
import { test, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import App from './App';

test('Renderiza el título de la aplicación', () => {
  render(<App />);
  // Busca el elemento que contenga el texto del título
  expect(screen.getByText(/Aplicación Fullstack con React/i)).toBeDefined();
});