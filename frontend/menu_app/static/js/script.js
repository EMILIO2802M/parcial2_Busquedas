// Mapeo de algoritmos
const algoritmos = {
    1: { nombre: 'Carretera USC', id: 'usc' },
    2: { nombre: 'Vuelos BFS', id: 'bfs' },
    3: { nombre: 'Vuelos DFS', id: 'dfs' }
};

const ciudadesPorAlgoritmo = {
    usc: [
        'Jiloyork', 'Sonora', 'Guanajuato', 'Oaxaca', 'Sinaloa',
        'Queretaro', 'Celaya', 'Zacatecas', 'Monterrey', 'Tamaulipas', 'CDMX'
    ],
    bfs: [
        'Jiloyork', 'Sonora', 'Guanajuato', 'Oaxaca', 'Sinaloa',
        'Queretaro', 'Celaya', 'Zacatecas', 'Monterrey', 'Tamaulipas', 'CDMX'
    ],
    dfs: [
        'Jiloyork', 'Sonora', 'Guanajuato', 'Oaxaca', 'Sinaloa',
        'Queretaro', 'Celaya', 'Zacatecas', 'Monterrey', 'Tamaulipas', 'CDMX'
    ]
};

function poblar_selects(algoritmoId) {
    const estadoInicial = document.getElementById('estado_inicial');
    const solucion = document.getElementById('solucion');
    const ciudades = ciudadesPorAlgoritmo[algoritmoId] || ciudadesPorAlgoritmo.bfs;

    estadoInicial.innerHTML = '';
    solucion.innerHTML = '';

    const placeholderInicial = document.createElement('option');
    placeholderInicial.value = '';
    placeholderInicial.textContent = 'Selecciona una ciudad';
    placeholderInicial.disabled = true;
    placeholderInicial.selected = true;
    estadoInicial.appendChild(placeholderInicial);

    const placeholderDestino = document.createElement('option');
    placeholderDestino.value = '';
    placeholderDestino.textContent = 'Selecciona una ciudad';
    placeholderDestino.disabled = true;
    placeholderDestino.selected = true;
    solucion.appendChild(placeholderDestino);

    ciudades.forEach((ciudad) => {
        const optionInicial = document.createElement('option');
        optionInicial.value = ciudad;
        optionInicial.textContent = ciudad;
        estadoInicial.appendChild(optionInicial);

        const optionDestino = document.createElement('option');
        optionDestino.value = ciudad;
        optionDestino.textContent = ciudad;
        solucion.appendChild(optionDestino);
    });

    estadoInicial.value = ciudades.includes('Jiloyork') ? 'Jiloyork' : ciudades[0];
    if (algoritmoId === 'usc') {
        solucion.value = ciudades.includes('Monterrey') ? 'Monterrey' : ciudades[ciudades.length - 1];
    } else {
        solucion.value = ciudades.includes('Monterrey') ? 'Monterrey' : ciudades[ciudades.length - 1];
    }
}

// Evento para seleccionar opción
function seleccionar_opcion(id) {
    const modal = document.getElementById('modal');
    const titulo = document.getElementById('modal-title');
    const algo = algoritmos[id];
    
    titulo.textContent = `Configurar - ${algo.nombre}`;
    
    // Guardar el algoritmo seleccionado
    document.getElementById('form-algoritmo').dataset.algoritmo = algo.id;
    poblar_selects(algo.id);
    
    // Limpiar resultados previos
    document.getElementById('resultado-container').style.display = 'none';
    document.getElementById('loading').style.display = 'none';
    document.getElementById('form-algoritmo').style.display = 'block';
    
    modal.style.display = 'block';
}

// Cerrar modal
function cerrar_modal() {
    const modal = document.getElementById('modal');
    modal.style.display = 'none';
}

// Cerrar modal al hacer click fuera
window.onclick = function(event) {
    const modal = document.getElementById('modal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

// Manejar envío del formulario
document.getElementById('form-algoritmo').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const algoritmo = this.dataset.algoritmo;
    const estado_inicial = document.getElementById('estado_inicial').value;
    const solucion = document.getElementById('solucion').value;
    
    // Mostrar loading
    document.getElementById('form-algoritmo').style.display = 'none';
    document.getElementById('loading').style.display = 'block';
    
    try {
        const response = await fetch('/ejecutar/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                algoritmo: algoritmo,
                estado_inicial: estado_inicial,
                solucion: solucion
            })
        });
        
        const data = await response.json();
        
        // Ocultar loading
        document.getElementById('loading').style.display = 'none';
        
        if (data.success) {
            mostrar_resultado(data.resultado);
        } else {
            mostrar_error(data.error);
        }
    } catch (error) {
        document.getElementById('loading').style.display = 'none';
        mostrar_error(`Error en la solicitud: ${error.message}`);
    }
});

// Mostrar resultado
function mostrar_resultado(resultado) {
    const container = document.getElementById('resultado-container');
    const resultadoDiv = document.getElementById('resultado');
    
    let html = '';
    
    if (resultado.encontrado) {
        html = `
            <p><strong>✓ Solución encontrada</strong></p>
            <p><strong>Tipo:</strong> ${resultado.tipo}</p>
        `;
        
        if (resultado.ruta) {
            html += `<p><strong>Ruta:</strong><br>${resultado.ruta.join(' → ')}</p>`;
        }
        
        if (resultado.destino) {
            html += `<p><strong>Destino final:</strong> ${resultado.destino}</p>`;
        }
        
        if (resultado.costo !== undefined) {
            html += `<p><strong>Costo total:</strong> ${resultado.costo} km</p>`;
        }
    } else {
        html = `<p><strong>✗ No se encontró solución</strong></p>
                <p>Verifica que el estado inicial y destino existan en el grafo.</p>`;
    }
    
    resultadoDiv.innerHTML = html;
    resultadoDiv.classList.remove('error');
    container.style.display = 'block';
}

// Mostrar error
function mostrar_error(error) {
    const container = document.getElementById('resultado-container');
    const resultadoDiv = document.getElementById('resultado');
    
    resultadoDiv.innerHTML = `<p><strong>Error:</strong> ${error}</p>`;
    resultadoDiv.classList.add('error');
    container.style.display = 'block';
}

// Obtener CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Agregar listener para botones con Enter
document.addEventListener('DOMContentLoaded', function() {
    poblar_selects('bfs');
});
