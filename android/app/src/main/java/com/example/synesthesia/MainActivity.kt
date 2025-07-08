package com.example.synesthesia

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.hardware.Sensor
import android.hardware.SensorEvent
import android.hardware.SensorEventListener
import android.hardware.SensorManager
import android.media.AudioManager
import android.media.ToneGenerator
import android.os.Bundle
import android.view.View
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity(), SensorEventListener {
    private lateinit var sensorManager: SensorManager
    private var accel: Sensor? = null
    private var gyro: Sensor? = null
    private lateinit var tone: ToneGenerator
    private lateinit var circleView: CircleView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        circleView = CircleView(this)
        setContentView(circleView)

        sensorManager = getSystemService(Context.SENSOR_SERVICE) as SensorManager
        accel = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)
        gyro = sensorManager.getDefaultSensor(Sensor.TYPE_GYROSCOPE)
        tone = ToneGenerator(AudioManager.STREAM_MUSIC, 100)
    }

    override fun onResume() {
        super.onResume()
        accel?.also { sensorManager.registerListener(this, it, SensorManager.SENSOR_DELAY_GAME) }
        gyro?.also { sensorManager.registerListener(this, it, SensorManager.SENSOR_DELAY_GAME) }
    }

    override fun onPause() {
        super.onPause()
        sensorManager.unregisterListener(this)
    }

    override fun onSensorChanged(event: SensorEvent) {
        if (event.sensor.type == Sensor.TYPE_ACCELEROMETER) {
            val freq = 440 + event.values[0] * 50
            tone.startTone(ToneGenerator.TONE_DTMF_S, 100)
        } else if (event.sensor.type == Sensor.TYPE_GYROSCOPE) {
            val intensity = kotlin.math.min(1f, kotlin.math.abs(event.values[0]) / 5f)
            circleView.radius = 100f + intensity * 200f
        }
    }

    override fun onAccuracyChanged(sensor: Sensor?, accuracy: Int) {}
}

class CircleView(context: Context) : View(context) {
    private val paint = Paint().apply { color = Color.CYAN }
    var radius: Float = 100f
        set(value) { field = value; invalidate() }

    override fun onDraw(canvas: Canvas) {
        super.onDraw(canvas)
        val cx = width / 2f
        val cy = height / 2f
        canvas.drawColor(Color.BLACK)
        canvas.drawCircle(cx, cy, radius, paint)
    }
}
