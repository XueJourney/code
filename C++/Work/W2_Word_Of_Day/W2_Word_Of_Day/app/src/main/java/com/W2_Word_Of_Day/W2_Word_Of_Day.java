
package com.W2_Word_Of_Day;

import android.app.Activity;
import android.widget.TextView;
import android.os.Bundle;

public class W2_Word_Of_Day extends Activity
{
    /** ���״δ����ʱ���á� */
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);

        /* ����һ�� TextView���������ı�����Ϊ "Hello world" */
        TextView  tv = new TextView(this);
        tv.setText("Hello World!");
        setContentView(tv);
    }
}
