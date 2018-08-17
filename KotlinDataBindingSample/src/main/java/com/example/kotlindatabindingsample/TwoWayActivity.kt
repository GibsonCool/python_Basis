package com.example.kotlindatabindingsample

import android.app.Activity
import android.os.Bundle

class TwoWayActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_list)
    }
}
