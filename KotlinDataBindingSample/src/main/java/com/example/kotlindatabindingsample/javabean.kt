package com.example.kotlindatabindingsample

import android.databinding.BaseObservable
import android.databinding.ObservableArrayMap
import android.databinding.ObservableBoolean
import android.databinding.ObservableField

class User(firstName: String, lastName: String, var isFired: ObservableBoolean = ObservableBoolean(false)) : BaseObservable() {
    var firstName: ObservableField<String> = ObservableField(firstName)
    var lastName: ObservableField<String> = ObservableField(lastName)
    val map: ObservableArrayMap<String, String> = ObservableArrayMap()

}