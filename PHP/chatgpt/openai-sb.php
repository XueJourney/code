<?php

$key = $_POST['key'];
$version = $_POST['version'];
$problem = $_POST['problem'];
$max_tokens = $_POST['max_tokens'];
$temperature = $_POST['temperature'];
$stream = $_POST['stream'];

$url = 'https://api.openai.com/v1/completions';

$headers = [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $key
];

$data = [
    'model' => $version,
    'prompt' => $problem,
    'max_tokens' => $max_tokens,
    'temperature' => $temperature,
    'top_p' => 1,
    'n' => 1,
    'stream' => $stream
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

$result = json_decode($response, true);

if ($stream) {
    // 处理流式返回结果
    while (!feof($ch)) {
        $chunk = fread($ch, 8192); // 读取一块数据
        if ($chunk !== false) {
            // 处理数据块，这里可以根据需要输出、存储或进行其他操作
            echo $chunk;
            // 如果需要流式地输出给客户端，可以使用flush()函数
            flush();
        }
    }
} else {
    // 处理非流式返回结果
    if ($result && isset($result['choices']) && count($result['choices']) > 0) {
        $choice = $result['choices'][0];
        $generatedText = $choice['text'];

        // 在这里可以对生成的文本进行处理，例如输出或保存到文件
        echo $generatedText;
    } else {
        // 处理错误或无效的响应
        echo "无效的响应或没有生成的文本可用。";
    }
}

?>