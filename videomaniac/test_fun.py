import upload_video, process_video, save_video

def upload():
    if request.method == 'POST':
        video = request.files['filename']
        print("filename")
        temp_video = upload_video(video)
        print("uploading video")
        processed_video = process_video(temp_video)
        print("processing video")
        saved_video = save_video(processed_video)
        print("saving video")
        flash("Thank you for uploading the video. Please see the details")
        render_template("public/upload.html", filename=saved_video)
        return render_template("public/upload.html", filename=saved_video)
    else:
        return render_template("public/upload.html")