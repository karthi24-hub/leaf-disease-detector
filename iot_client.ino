/*
  ESP32-CAM STABLE NITRO (Anti-Overflow Edition)
*/

#include "esp_camera.h"
#include <WiFi.h>
#include "esp_http_server.h"

const char* ssid = "Karthis_WIFI";
const char* password = "krishiga13";

// AI THINKER PINS
#define PWDN_GPIO_NUM     32
#define RESET_GPIO_NUM    -1
#define XCLK_GPIO_NUM      0
#define SIOD_GPIO_NUM     26
#define SIOC_GPIO_NUM     27
#define Y9_GPIO_NUM       35
#define Y8_GPIO_NUM       34
#define Y7_GPIO_NUM       39
#define Y6_GPIO_NUM       36
#define Y5_GPIO_NUM       21
#define Y4_GPIO_NUM       19
#define Y3_GPIO_NUM       18
#define Y2_GPIO_NUM        5
#define VSYNC_GPIO_NUM    25
#define HREF_GPIO_NUM     23
#define PCLK_GPIO_NUM     22

#define PART_BOUNDARY "123456"
static const char* STREAM_CONTENT_TYPE = "multipart/x-mixed-replace;boundary=" PART_BOUNDARY;
static const char* STREAM_BOUNDARY = "\r\n--" PART_BOUNDARY "\r\n";
static const char* STREAM_PART = "Content-Type: image/jpeg\r\nContent-Length: %u\r\n\r\n";

httpd_handle_t camera_httpd = NULL;

static esp_err_t stream_handler(httpd_req_t *req) {
  camera_fb_t * fb = NULL;
  char buf[64];
  esp_err_t res = ESP_OK;

  httpd_resp_set_type(req, STREAM_CONTENT_TYPE);

  while (true) {
    fb = esp_camera_fb_get();
    if (!fb) {
      delay(5); // Wait if buffer is full
      continue;
    }

    size_t hlen = snprintf(buf, 64, STREAM_PART, fb->len);
    res = httpd_resp_send_chunk(req, buf, hlen);
    if(res == ESP_OK) res = httpd_resp_send_chunk(req, (const char*)fb->buf, fb->len);
    if(res == ESP_OK) res = httpd_resp_send_chunk(req, STREAM_BOUNDARY, strlen(STREAM_BOUNDARY));

    esp_camera_fb_return(fb);
    if(res != ESP_OK) break;
    
    // 🔴 Give the hardware time to clear the buffer
    delay(20); 
  }
  return res;
}

void startCameraServer() {
  httpd_config_t config = HTTPD_DEFAULT_CONFIG();
  config.server_port = 81;
  config.task_priority = 5; // Low priority to avoid stalling
  
  httpd_uri_t stream_uri = { .uri = "/", .method = HTTP_GET, .handler = stream_handler, .user_ctx = NULL };
  httpd_start(&camera_httpd, &config);
  httpd_register_uri_handler(camera_httpd, &stream_uri);
}

void setup() {
  Serial.begin(115200);

  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sccb_sda = SIOD_GPIO_NUM;
  config.pin_sccb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 10000000;   
  config.pixel_format = PIXFORMAT_JPEG;
  
  // STABLE LIVE SETTINGS
  config.frame_size = FRAMESIZE_QVGA; 
  config.jpeg_quality = 15;           
  config.fb_count = 2; // Use two buffers for smooth handover
  config.grab_mode = CAMERA_GRAB_LATEST;

  if (esp_camera_init(&config) != ESP_OK) return;

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) delay(500);

  Serial.println("\n--- CAMERA READY ---");
  Serial.print("Stream: http://");
  Serial.print(WiFi.localIP());
  Serial.println(":81");

  startCameraServer();
}

void loop() { delay(1); }
