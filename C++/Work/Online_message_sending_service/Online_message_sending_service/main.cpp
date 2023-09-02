#include <iostream>
#include <string>
#include <sstream>
#include <curl/curl.h>
#include <openssl/md5.h>
#include <map>
#include <fstream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

const std::string smsapi = "http://api.smsbao.com/";

std::string md5(const std::string& str) {
    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5((const unsigned char*)str.c_str(), str.size(), digest);
    std::stringstream ss;
    for (int i = 0; i < MD5_DIGEST_LENGTH; ++i) {
        ss << std::hex << static_cast<int>(digest[i]);
    }
    return ss.str();
}

std::string statusStr(const std::string& statusCode) {
    std::map<std::string, std::string> statusMap = {
        {"0", "短信发送成功"},
        {"-1", "参数不全"},
        {"-2", "服务器空间不支持，请确认支持curl或者fsocket，联系您的空间商解决或者更换空间"},
        {"30", "密码错误"},
        {"40", "账号不存在"},
        {"41", "余额不足"},
        {"42", "账户已过期"},
        {"43", "IP地址限制"},
        {"50", "内容含有敏感词"}
    };

    if (statusMap.find(statusCode) != statusMap.end()) {
        return statusMap[statusCode];
    }
    else {
        return "未知状态码";
    }
}

class SMS {
private:
    std::string user;
    std::string password;

public:
    SMS(const std::string& username, const std::string& passwd) : user(username), password(passwd) {}

    void send_ms(const std::string& phone, const std::string& content) {
        std::string data = "u=" + user + "&p=" + md5(password) + "&m=" + phone + "&c=" + content;
        std::string send_url = smsapi + "sms?" + data;

        // Use libcurl to perform HTTP request
        CURL* curl = curl_easy_init();
        if (curl) {
            curl_easy_setopt(curl, CURLOPT_URL, send_url.c_str());
            CURLcode res = curl_easy_perform(curl);
            if (res != CURLE_OK) {
                std::cerr << "Failed to send SMS: " << curl_easy_strerror(res) << std::endl;
            }
            curl_easy_cleanup(curl);
        }
    }
};

int main() {
    std::string user = "Mr_Xue";
    std::string password = "ec65ec719082e7bd172f81f907e85cf4";
    SMS sms(user, password);

    std::string phone, content;
    std::cout << "Enter recipient's phone number: ";
    std::cin >> phone;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cout << "Enter SMS content: ";
    std::getline(std::cin, content);

    sms.send_ms(phone, content);

    return 0;
}