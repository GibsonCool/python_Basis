package com.example.kotlindatabindingsample

import android.app.Activity
import android.content.Intent
import android.databinding.DataBindingUtil
import android.os.Bundle
import android.support.v4.content.ContextCompat.startActivity
import android.view.View
import com.example.kotlindatabindingsample.databinding.ActivityMainBinding

class MainActivity : Activity() {

    var mBinding: ActivityMainBinding? = null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        mBinding = DataBindingUtil.setContentView(this, R.layout.activity_main)
        mBinding?.presenter = Presenter()
    }


    class Presenter {
        fun onClickSimpleDemo(view: View) {
            startActivity(view.context, Intent(view.context, SimpleActivity::class.java), null)
        }
    }
}
