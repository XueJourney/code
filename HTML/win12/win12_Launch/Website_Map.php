<?php
// 设置网站的根目录
$rootDirectory = $_SERVER['DOCUMENT_ROOT'];

// 创建一个数组来存储网站地图链接
$sitemapLinks = [];

// 递归函数，用于遍历目录和子目录下的文件
function generateSitemapLinks($directory, $relativePath = '') {
    global $sitemapLinks;
    $excludedFiles = ['404.html','Website_Map.php']; // 要排除的文件名列表
    
    $files = scandir($directory);
    
    foreach ($files as $file) {
        if ($file == '.' || $file == '..') {
            continue;
        }
        
        $filePath = $directory . '/' . $file;
        $fileRelativePath = $relativePath . '/' . $file;
        
        // 检查文件是否以.html或.php结尾，且不在排除列表中
        if (is_file($filePath) && (pathinfo($file, PATHINFO_EXTENSION) == 'html' || pathinfo($file, PATHINFO_EXTENSION) == 'php') && !in_array($file, $excludedFiles)) {
            // 构建链接
            $url = 'https://www.windows12.top' . $fileRelativePath;
            $sitemapLinks[] = $url;
        } elseif (is_dir($filePath)) {
            // 如果是目录，继续递归
            generateSitemapLinks($filePath, $fileRelativePath);
        }
    }
}

// 调用递归函数开始生成网站地图链接
generateSitemapLinks($rootDirectory);

// 输出XML格式的网站地图
header('Content-Type: application/xml; charset=utf-8');

echo '<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">';

foreach ($sitemapLinks as $link) {
    echo '<url>';
    echo '<loc>' . htmlspecialchars($link) . '</loc>';
    echo '</url>';
}

echo '</urlset>';
?>