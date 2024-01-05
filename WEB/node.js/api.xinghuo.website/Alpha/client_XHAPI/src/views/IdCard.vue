<template>
  <div class="api-documentation">
    <button class="back-button" @click="goBack">返回</button>

    <h1>身份证信息核验接口文档</h1>

    <h2>接口地址</h2>
    <p>https://api.xinghuo.website/api/idcard</p>

    <h2>返回格式</h2>
    <p>JSON</p>

    <h2>请求方式</h2>
    <p>GET & POST</p>

    <div class="copy-container">
      <code id="request-example"
        >https://api.xinghuo.website/api/idcard?idcard=123456789101&name=张三</code
      >
      <button @click="copyToClipboard('#request-example')">复制</button>
    </div>

    <h2>接口信息</h2>
    <table>
      <thead>
        <tr>
          <th>接口名称</th>
          <th>是否必填</th>
          <th>接口类型</th>
          <th>接口说明</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>idcard</td>
          <td>是</td>
          <td>string</td>
          <td>身份证信息</td>
        </tr>
        <tr>
          <td>name</td>
          <td>是</td>
          <td>string</td>
          <td>姓名</td>
        </tr>
      </tbody>
    </table>

    <h2>返回参数</h2>
    <thead>
      <tr>
        <th>接口名称</th>
        <th>接口类型</th>
        <th>接口说明</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>code</td>
        <td>string</td>
        <td>返回码，0：成功，非0：失败</td>
      </tr>
      <tr>
        <td>message</td>
        <td>string</td>
        <td>返回码说明(成功/失败)</td>
      </tr>
      <tr>
        <td>result</td>
        <td>json</td>
        <td>实名信息</td>
      </tr>
      <tr>
        <td>result.name</td>
        <td>string</td>
        <td>姓名</td>
      </tr>
      <tr>
        <td>result.idcard</td>
        <td>string</td>
        <td>身份证号</td>
      </tr>
      <tr>
        <td>result.res</td>
        <td>string</td>
        <td>核验结果状态码，1 一致；2 不一致；3 无记录</td>
      </tr>
      <tr>
        <td>result.description</td>
        <td>string</td>
        <td>核验结果状态描述(如:一致)</td>
      </tr>
      <tr>
        <td>result.sex</td>
        <td>string</td>
        <td>性别(男/女)</td>
      </tr>
      <tr>
        <td>result.birthday</td>
        <td>string</td>
        <td>生日</td>
      </tr>
      <tr>
        <td>result.address</td>
        <td>string</td>
        <td>住址</td>
      </tr>
    </tbody>
  </div>
</template>

<script>
export default {
  name: 'ApiDocumentation',
  methods: {
    copyToClipboard(selector) {
      const el = document.querySelector(selector)
      if (el) {
        const range = document.createRange()
        range.selectNode(el)
        window.getSelection().removeAllRanges()
        window.getSelection().addRange(range)
        try {
          document.execCommand('copy')
          window.getSelection().removeAllRanges()
          alert('复制成功！')
        } catch (e) {
          alert('复制失败')
        }
      }
    },
    goBack() {
      // 逻辑来处理返回操作
      window.history.back()
    }
  }
}
</script>

<style scoped>
.api-documentation {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  background: var(--background-color);
  color: var(--text-color);
}

.back-button {
  position: absolute;
  padding: 10px 20px;
  background-color: #4caf50; /* Green */
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.back-button:hover {
  background-color: #45a049;
}

h1,
h2 {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1 {
  text-align: center;
}

table {
  border-collapse: collapse;
  margin-top: 10px;
  width: 100%;
}

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: var(
    --background-color,
    #f2f2f2
  ); /* Default to a light grey if the variable is not set */
}

code {
  background-color: var(--background-color);
  padding: 5px;
  border-radius: 5px;
  font-family: 'Courier New', Courier, monospace;
}

button {
  background-color: #4caf50; /* Green */
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 5px;
}

button:hover {
  background-color: #45a049;
}

@media screen and (max-width: 600px) {
  .api-documentation {
    width: 100%;
    box-shadow: none;
    border-radius: 0;
  }
}

.copy-container {
  display: flex;
  align-items: center;
}

.copy-container code {
  margin-right: 10px;
}
</style>
