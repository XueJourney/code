
package com.W2_Word_Of_Day;

import android.app.Activity;
import android.widget.TextView;
import android.os.Bundle;

public class W2_Word_Of_Day extends Activity
{
    /** 在首次创建活动时调用。 */
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);

        /* 创建一个 TextView，并将其文本设置为 "Hello world" */
        TextView  tv = new TextView(this);
        tv.setText("Hello World!");
        setContentView(tv);
    }
}
