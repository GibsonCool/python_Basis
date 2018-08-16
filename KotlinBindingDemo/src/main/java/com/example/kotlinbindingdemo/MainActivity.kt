package com.example.kotlinbindingdemo

import android.databinding.BindingAdapter
import android.databinding.DataBindingUtil
import android.databinding.ObservableBoolean
import android.databinding.ObservableField
import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.util.Log
import android.view.View
import android.widget.TextView
import android.widget.Toast
import com.example.kotlinbindingdemo.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    var binding: ActivityMainBinding? = null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main)
        binding?.user = User(" Gibson", "Cool", 24)
        binding?.userOb = UserObservable(ObservableField("cxx"), ObservableField("www.baidu.com"))
        binding?.imgInfo = ImageInfo(ObservableBoolean(true), ObservableField("s"))
        binding?.viewSubbb?.viewStub?.inflate()
        binding?.presenter = Presenter()

    }

    inner class Presenter {
        fun textChange(text: CharSequence, start: Int, lengthBefore: Int, lengthAfter: Int) {
            Log.e("cxxinfo", text.toString())
            var user = binding?.user
            user?.age = text.length
            binding?.user = user

        }

        fun changeObservableName(view: View) {
            Toast.makeText(view.context, "change", Toast.LENGTH_SHORT).show()
            binding?.userOb?.name?.set("name changed by buttondd")
        }

        fun changeImage(info: ImageInfo) {
            info.url.set(if (info.tag.get()) "this is true tag" else "this is FALSE tag")
            info.tag.set(!info.tag.get())
        }

    }
}


@BindingAdapter("app:url")
fun changeInfoByBindingAdapter(view: TextView, info: String) {
    Log.e("cxxinfo", "changeImgByBindingAdapter   info:$info")
    view.text =  info
}







