package com.example.kotlinbindingdemo

import android.databinding.ObservableBoolean
import android.databinding.ObservableField

data class User(var firstName: String, var lastName: String, var age: Int)

data class UserObservable(var name: ObservableField<String>, var url: ObservableField<String>)

data class ImageInfo(var tag:ObservableBoolean , var url: ObservableField<String>)