# %%
import os
import shutil

from pydub import AudioSegment
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


def load_audio(file_path):
    audio = AudioSegment.from_file(file_path, format="mp3")
    audio_array = np.array(audio.get_array_of_samples()).squeeze()
    return audio, audio_array


def find_marker_positions(
    main_audio_array,
    marker_sound_array,
    downsampling_factor=1000,
):
    main_audio_downsampled = main_audio_array[::downsampling_factor].astype(np.float32)
    marker_sound_downsampled = marker_sound_array[::downsampling_factor].astype(
        np.float32
    )
    marker_sound_downsampled -= np.mean(marker_sound_downsampled)

    marker_length = len(marker_sound_downsampled)
    correlation_coefficients = []

    for i in range(len(main_audio_downsampled) - marker_length + 1):
        window = main_audio_downsampled[i : i + marker_length]
        window -= np.mean(window)
        correlation_coef = np.corrcoef(window, marker_sound_downsampled)[0, 1]
        correlation_coefficients.append(correlation_coef)

    correlation_coefficients = np.array(correlation_coefficients)
    peaks, _ = find_peaks(
        correlation_coefficients, height=0.5, distance=1.5e6 // downsampling_factor
    )
    marker_positions = [
        (peak + marker_length // 2) * downsampling_factor for peak in peaks
    ]

    return marker_positions, correlation_coefficients, peaks


def save_segments(main_audio, main_audio_array, marker_positions):
    output_dir = os.path.expanduser("~/Downloads/mp3/")
    # Delete the directory if it exists, then create it
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    for i, time in enumerate(marker_positions):
        start_time = 0 if i == 0 else marker_positions[i - 1]
        end_time = time
        segment_array = main_audio_array[start_time:end_time]
        segment = AudioSegment(
            segment_array.tobytes(),
            frame_rate=main_audio.frame_rate,
            sample_width=main_audio.sample_width,
            channels=main_audio.channels,
        )
        segment.export(f"{output_dir}{i + 1:03}.mp3", format="mp3")

    print(f"Split {len(marker_positions) + 1} segments successfully!")


# %%
# Load the main audio file and the marker sound
main_audio, main_audio_array = load_audio("sample_data/01.mp3")
marker_sound, marker_sound_array = load_audio("sample_data/mark_sound.mp3")

# %%
# Detect marker positions
marker_positions, correlation_coefficients, peaks = find_marker_positions(
    main_audio_array, marker_sound_array
)
plt.plot(correlation_coefficients, label="Correlation Coefficients")
plt.plot(peaks, correlation_coefficients[peaks], "x", label="Peaks")
print(len(marker_positions))
# %%
# Save splitted segments into mp3 files
save_segments(main_audio, main_audio_array, marker_positions)
