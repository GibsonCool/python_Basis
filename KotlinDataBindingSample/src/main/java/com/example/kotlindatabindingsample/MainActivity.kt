package com.example.kotlindatabindingsample

import android.app.Activity
import android.content.Intent
import android.databinding.DataBindingUtil
import android.os.Bundle
import android.support.v4.content.ContextCompat.startActivity
import android.view.View
import android.widget.Toast
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

        fun onClickListDemo(view: View) {
            startActivity(view.context, Intent(view.context, ListActivity::class.java), null)
        }

        fun onClickTwoWayDemo(view: View) {
            startActivity(view.context, Intent(view.context, TwoWayActivity::class.java), null)
        }

        fun onClickExpressionDemo(view: View) {
            startActivity(view.context, Intent(view.context, ExpressionActivity::class.java), null)
        }

        fun onClickAnimationDemo(view: View) {
            startActivity(view.context, Intent(view.context, AnimationActivity::class.java), null)
        }

        fun onClickLambdaDemo(view: View) {
            startActivity(view.context, Intent(view.context, LambdaActivity::class.java), null)
        }

        fun onClickInjectDemo(view: View) {
            Toast.makeText(view.context,"onCickInjectDemo",Toast.LENGTH_SHORT).show()
//            if (DemoApplication.isTest) {
//                DataBindingUtil.setDefaultComponent(ProductionComponent())
//            } else {
//                DataBindingUtil.setDefaultComponent(TestComponent())
//            }
//            DemoApplication.isTest = !DemoApplication.isTest
//            recreate()
        }
    }
}
