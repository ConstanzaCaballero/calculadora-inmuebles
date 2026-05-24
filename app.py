from flask import Flask, render_template, request
from dataclasses import dataclass

app = Flask(__name__)


@dataclass
class ResultadoCalculo:
    renta_anual: float
    gastos_anuales: float
    ingreso_neto_anual: float
    rentabilidad_bruta: float
    rentabilidad_neta: float
    veredicto: str
    razon: str


def calcular_rentabilidad(
    precio_compra: float,
    alquiler_mensual: float,
    gastos_mensuales: float,
) -> ResultadoCalculo:
    renta_anual = alquiler_mensual * 12
    gastos_anuales = gastos_mensuales * 12
    ingreso_neto_anual = renta_anual - gastos_anuales

    rentabilidad_bruta = (renta_anual / precio_compra) * 100
    rentabilidad_neta = (ingreso_neto_anual / precio_compra) * 100

    if rentabilidad_neta >= 6:
        veredicto = "COMPRAR"
        razon = f"Rentabilidad neta del {rentabilidad_neta:.2f}% es sólida (≥6%)."
    elif rentabilidad_neta >= 4:
        veredicto = "CONSIDERAR"
        razon = f"Rentabilidad neta del {rentabilidad_neta:.2f}% es aceptable (4–6%) — evalúa ubicación y revalorización."
    else:
        veredicto = "NO COMPRAR"
        razon = f"Rentabilidad neta del {rentabilidad_neta:.2f}% es baja (<4%) — el retorno puede no justificar la inversión."

    return ResultadoCalculo(
        renta_anual=renta_anual,
        gastos_anuales=gastos_anuales,
        ingreso_neto_anual=ingreso_neto_anual,
        rentabilidad_bruta=rentabilidad_bruta,
        rentabilidad_neta=rentabilidad_neta,
        veredicto=veredicto,
        razon=razon,
    )


@app.route("/", methods=["GET", "POST"])
def index():
    resultado: ResultadoCalculo | None = None
    error: str | None = None
    valores = {}

    if request.method == "POST":
        try:
            precio_compra = float(request.form["precio_compra"].replace(",", ""))
            alquiler_mensual = float(request.form["alquiler_mensual"].replace(",", ""))
            gastos_mensuales = float(request.form["gastos_mensuales"].replace(",", ""))

            if any(v <= 0 for v in [precio_compra, alquiler_mensual]):
                raise ValueError("El precio y el alquiler deben ser mayores que cero.")

            if gastos_mensuales < 0:
                raise ValueError("Los gastos no pueden ser negativos.")

            valores = request.form
            resultado = calcular_rentabilidad(precio_compra, alquiler_mensual, gastos_mensuales)
        except ValueError as e:
            error = str(e) if str(e) else "Por favor, introduce valores numéricos válidos."
            valores = request.form

    return render_template("index.html", resultado=resultado, error=error, valores=valores)


if __name__ == "__main__":
    app.run(debug=True)
