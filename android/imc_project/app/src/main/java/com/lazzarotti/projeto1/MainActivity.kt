package com.lazzarotti.projeto1

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_main.*
import java.lang.Math.round

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val btCalcular = calcular
        val resultado = resultado

        btCalcular.setOnClickListener {

            val peso = peso.text.toString().toDouble()
            val altura = altura.text.toString().toDouble()

            var calculo: Double = (peso/(altura*altura/10000))
            calculo = round(calculo).toDouble()

            if(calculo < 18.5)
                resultado.setText("Peso: " + peso + "\nAltura: " + altura + "\nResultado: " + calculo + "\nAbaixo do peso.")
            else if(calculo >= 18.5 && calculo <= 24.9)
                resultado.setText("Peso: " + peso + "\nAltura: " + altura + "\nResultado: " + calculo + "\nPeso Normal.")
            else if(calculo >= 25 && calculo <= 29.9)
                resultado.setText("Peso: " + peso + "\nAltura: " + altura + "\nResultado: " + calculo + "\nSobrepeso.")
            else if(calculo >= 30 && calculo <= 34.9)
                resultado.setText("Peso: " + peso + "\nAltura: " + altura + "\nResultado: " + calculo + "\nObesidade Grau I.")
            else if(calculo >= 35 && calculo <= 39.9)
                resultado.setText("Peso: " + peso + "\nAltura: " + altura + "\nResultado: " + calculo + "\nObesidade Grau II.")
            else if(calculo >= 40)
                resultado.setText("Peso: " + peso + "\nAltura: " + altura + "\nResultado: " + calculo + "\nObesidade Grau III ou Mórbida.")
            else
                resultado.setText("Valor inválido, verifique os números digitados.")

        }
    }
}