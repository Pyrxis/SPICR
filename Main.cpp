#include <iostream>
#include <opencv2/opencv.hpp>
#include <string>
#include <fstream>


using namespace std;
using namespace cv;

Point pt1(0, 0);
Point pt2(360, 182);

bool ex(String file) {
	std::ifstream fin(file);

	if (fin) {
		return true;
	}
	else {
		return false;
	}

}

bool ftest(Mat framex) {
	Mat frame = framex.clone();
	int colorpixeln = 0;
	int threshold = 30;

	int bluelowrange = 1;
	int bluehighrange = 100;

	int greenlowrange = -1;
	int greenhighrange = 100;

	int redlowrange = 120;
	int redhighrange = 260;

	for (int j = pt1.x; j < pt2.x; j++) {
		for (int i = pt1.y; i < pt2.y; i++) {
			Vec3b pixel = frame.at<Vec3b>(i, j);
			int blue = pixel.val[0];
			int green = pixel.val[1];
			int red = pixel.val[2];

			if (blue >= bluelowrange && blue <= bluehighrange) {

				if (green >= greenlowrange && green <= greenhighrange) {

					if (red >= redlowrange && red <= redhighrange) {
						colorpixeln++;
					}
				}
			}
			blue = 0;
			green = 0;
			red = 0;
		}
	}
	frame.release();
	
	if (colorpixeln > threshold) {
		return true;
	}
	else {
		return false;
	}
}


int main()
{


	int numbofpanes = 8;

	Mat frame1 = imread("C:/Users/jongee/Desktop/panel1.jpg");
	Mat frame2 = imread("C:/Users/jongee/Desktop/panel2.jpg");
	Mat frame3 = imread("C:/Users/jongee/Desktop/panel3.jpg");
	Mat frame4 = imread("C:/Users/jongee/Desktop/panel4.jpg");
	Mat frame5 = imread("C:/Users/jongee/Desktop/panel5.jpg");
	Mat frame6 = imread("C:/Users/jongee/Desktop/panel6.jpg");
	Mat frame7 = imread("C:/Users/jongee/Desktop/panel7.jpg");
	Mat frame8 = imread("C:/Users/jongee/Desktop/panel8.jpg");
	
	
	Mat edges;
		for (int i = 0; i < numbofpanes; i++) {
			switch (i) {
			case 0: 
				
				if (ftest(frame1)) {
					imwrite("C:/Users/jongee/Desktop/problem/panel" + std::to_string(i+1) + ".jpg", frame1);
				}
				else {
					imwrite("C:/Users/jongee/Desktop/safe/panel" + std::to_string(i+1) + ".jpg", frame1);
				}
				
				break;
			case 1: 	
				
				if (ftest(frame2)) {
					imwrite("C:/Users/jongee/Desktop/problem/panel" + std::to_string(i+1) + ".jpg", frame2);
				}
				else {
					imwrite("C:/Users/jongee/Desktop/safe/panel" + std::to_string(i + 1) + ".jpg", frame2);
				}
				
				break;
			case 2:
				if (ftest(frame3)) {
					imwrite("C:/Users/jongee/Desktop/problem/panel" + std::to_string(i + 1) + ".jpg", frame3);
				}
				else {
					imwrite("C:/Users/jongee/Desktop/safe/panel" + std::to_string(i + 1) + ".jpg", frame3);
				}
				break;
			case 3: 
				if (ftest(frame4)) {
					imwrite("C:/Users/jongee/Desktop/problem/panel" + std::to_string(i+1) + ".jpg", frame2);
				}
				else {
					imwrite("C:/Users/jongee/Desktop/safe/panel" + std::to_string(i+1) + ".jpg", frame2);
				}
				break;
			case 4: 
				if (ftest(frame5)) {
					imwrite("C:/Users/jongee/Desktop/problem/panel" + std::to_string(i + 1) + ".jpg", frame5);
				}
				else {
					imwrite("C:/Users/jongee/Desktop/safe/panel" + std::to_string(i + 1) + ".jpg", frame5);
				}
				break;
			case 5: 
				if (ftest(frame6)) {
					imwrite("C:/Users/jongee/Desktop/problem/panel" + std::to_string(i + 1) + ".jpg", frame6);
				}
				else {
					imwrite("C:/Users/jongee/Desktop/safe/panel" + std::to_string(i + 1) + ".jpg", frame6);
				}
				break;
			case 6:
				if (ftest(frame7)) {
					imwrite("C:/Users/jongee/Desktop/problem/panel" + std::to_string(i + 1) + ".jpg", frame7);
				}
				else {
					imwrite("C:/Users/jongee/Desktop/safe/panel" + std::to_string(i + 1) + ".jpg", frame7);
				}
				break;
			case 7: 
				if (ftest(frame8)) {
					imwrite("C:/Users/jongee/Desktop/problem/panel" + std::to_string(i + 1) + ".jpg", frame8);
				}
				else {
					imwrite("C:/Users/jongee/Desktop/safe/panel" + std::to_string(i + 1) + ".jpg", frame8);
				}
				break;
			}
			

		}
	
	return 0;
}

 
