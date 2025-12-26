import os
from datetime import timedelta
from moviepy.video.io.VideoFileClip import VideoFileClip




def get_video_duration(file_path):
    """使用moviepy获取视频时长（秒）"""
    try:
        clip = VideoFileClip(file_path)
        duration = clip.duration
        clip.close()
        return duration
    except Exception as e:
        print(f"无法获取文件 {file_path} 的时长: {e}")
        return 0

def format_duration(seconds):
    """将秒数格式化为 HH:MM:SS"""
    return str(timedelta(seconds=seconds))


def calculate_total_duration(folder_path):
    """计算文件夹中所有MP4文件的总时长"""
    total_seconds = 0
    video_count = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.mp4'):
                file_path = os.path.join(root, file)
                duration = get_video_duration(file_path)
                total_seconds += duration
                video_count += 1
                print(f"已处理: {file} - 时长: {format_duration(duration)}")

    return total_seconds, video_count


if __name__ == "__main__":
    folder_path = input("请输入文件夹路径: ").strip()

    if not os.path.isdir(folder_path):
        print("错误: 指定的路径不是有效的文件夹")
    else:
        total_seconds, video_count = calculate_total_duration(folder_path)
        print("\n统计结果:")
        print(f"视频文件总数: {video_count}")
        print(f"总时长: {format_duration(total_seconds)} (HH:MM:SS)")



