package com.example.synesthesia

import android.content.Context
import androidx.test.core.app.ApplicationProvider
import org.junit.Assert.assertEquals
import org.junit.Test

class CircleViewTest {
    @Test
    fun radius_updates() {
        val context = ApplicationProvider.getApplicationContext<Context>()
        val view = CircleView(context)
        view.radius = 50f
        assertEquals(50f, view.radius)
    }
}
