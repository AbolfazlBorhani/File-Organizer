#include "fileorganizer.h"
#include "./ui_fileorganizer.h"

FileOrganizer::FileOrganizer(QWidget *parent): QMainWindow(parent), ui(new Ui::FileOrganizer) {
    ui->setupUi(this);
}

FileOrganizer::~FileOrganizer() {
    delete ui;
}

str FileOrganizer::GetPath() const {
    str text{ ui->Path->text().toUtf8().toStdString() };

    if (text.find('\\') < 100) {
        for (std::size_t i{ 0 }; i < text.length(); ++i) {
            if (text.at(i) == '\\') {
                text.replace(i, 1, "/");
            }
        }
    }

    if (!text.ends_with("/")) {
        text.append("/");
    }

    return text;
}

bool FileOrganizer::ChackExistsDirectory(str& path) {
    if (fs::exists(path) && fs::is_directory(path)) {
        return true;
    }

    else {
        return false;
    }
}

void FileOrganizer::ClearAllVectors() {
    this->Files.clear();
    // this->TXT.clear();
    // this->PNG.clear();
    // this->JPG.clear();
    // this->MP4.clear();
    // this->MKV.clear();
    // this->MOV.clear();
    // this->MP3.clear();
    // this->GIF.clear();
    // this->WEBP.clear();
    // this->WEBM.clear();
    // this->HEIC.clear();
    // this->ETC.clear();
}

bool FileOrganizer::SaveFilesNames() {
    this->ClearAllVectors();
    this->Path = this->GetPath();

    if (!this->ChackExistsDirectory(this->Path)) {
        this->Warning("None", 2);
        return false;
    }

    if (fs::is_empty(this->Path)) {
        this->Warning("None", 3);
        return false;
    }

    else {
        try {
            for (const auto& entry : fs::directory_iterator(this->Path)) {
                if (fs::is_regular_file(entry.path())) {
                    str FileName{ entry.path().string().substr(this->Path.size(), entry.path().string().length() - 1) };

                    if (FileName.ends_with("txt"))
                        this->Files["TXT"].push_back(FileName);
                    else if (FileName.ends_with("png") or FileName.ends_with("PNG"))
                        this->Files["PNG"].push_back(FileName);
                    else if (FileName.ends_with("jpg") or FileName.ends_with("JPG"))
                        this->Files["JPG"].push_back(FileName);
                    else if (FileName.ends_with("mp4") or FileName.ends_with("MP4"))
                        this->Files["MP4"].push_back(FileName);
                    else if (FileName.ends_with("mkv") or FileName.ends_with("MKV"))
                        this->Files["MKV"].push_back(FileName);
                    else if (FileName.ends_with("mov") or FileName.ends_with("MOV"))
                        this->Files["MOV"].push_back(FileName);
                    else if (FileName.ends_with("mp3") or FileName.ends_with("MP3"))
                        this->Files["MP3"].push_back(FileName);
                    else if (FileName.ends_with("gif") or FileName.ends_with("GIF"))
                        this->Files["GIF"].push_back(FileName);
                    else if (FileName.ends_with("webp") or FileName.ends_with("WEBP"))
                        this->Files["WEBP"].push_back(FileName);
                    else if (FileName.ends_with("webm") or FileName.ends_with("WEBM"))
                        this->Files["WEBM"].push_back(FileName);
                    else if (FileName.ends_with("heic") or FileName.ends_with("HEIC"))
                        this->Files["HEIC"].push_back(FileName);
                    else
                        this->Files["ETC"].push_back(FileName);
                }
            }
            return true;
        }

        catch (const std::exception &e) {
            ui->Logs->append("Error: " + QString(e.what()));
        }
    }
}

void FileOrganizer::Warning(QString Format, int Case) {
    switch (Case) {
    case 1:
        ui->Logs->append("Warning: There is no " + Format + " file or your request is invalid.");
        break;

    case 2:
        ui->Logs->append("Warning: This directory does not exists !");
        break;

    case 3:
        ui->Logs->append("Warning: This directory is empty !");
        break;

    default:
        ui->Logs->append("Warning: Incorrect input !");
        break;
    }
}

void FileOrganizer::on_Show_clicked() {
    ui->Logs->clear();
    ui->Logs->append("\t\t   *** Show Directory ***\n");

    if (this->SaveFilesNames()) {
        for (const auto& pair : this->Files) {
            if (!pair.second.empty()) {
                int index{ 0 };
                ui->Logs->append(QString::fromStdString(pair.first));
                for (const auto& value : pair.second) {
                    ui->Logs->append('[' + QString::number(++index) +
                                     '/' + QString::number(pair.second.size()) +
                                     "] -- " + QString::fromStdString(value));
                }
                ui->Logs->append("");
            }
        }
    }
}

void FileOrganizer::on_Categories_clicked() {
    ui->Logs->clear();
    ui->Logs->append("\t\t    *** Categories ***\n");

    if (this->SaveFilesNames()) {
        ui->Logs->append("New Directoires:");
        for (const auto& pair : this->Files) {
            if (!pair.second.empty()) {
                str NewPath{ this->Path + pair.first + '/' };
                if (!fs::exists(NewPath)) {
                    fs::create_directory(NewPath);

                    for (const auto& value : pair.second) {
                        fs::rename(this->Path + value, NewPath + value);
                    }

                    ui->Logs->append("+ " + QString::fromStdString(pair.first) +
                                     "[+" + QString::number(pair.second.size()) +
                                     " Files]");
                }
            }
        }
    }
}

void FileOrganizer::on_Rename_clicked() {
    ui->Logs->clear();
    ui->Logs->append("\t\t      *** Rename ***\n");

    if (this->SaveFilesNames()) {
        bool flag{ false };

        for (const auto& pair : this->Files) {
            if (QString::fromStdString(pair.first) == ui->RenameComboBox->currentText()) {
                int index{ 0 };
                for (const auto& value : pair.second) {
                    fs::rename(this->Path + value, this->Path + std::to_string(++index) + "." + pair.first);
                    ui->Logs->append("- " + QString::fromStdString(value));
                }

                ui->Logs->append("\nResult: "
                                 + QString::number(pair.second.size()) + ' '
                                 + QString::fromStdString(pair.first)
                                 + " files have been successfully renamed.");

                flag = true;
                break;
            }
        }

        if (!flag) {
            this->Warning(ui->RenameComboBox->currentText(), 1);
        }
    }
}

void FileOrganizer::on_Delete_clicked() {
    ui->Logs->clear();
    ui->Logs->append("\t\t      *** Delete ***\n");

    if (this->SaveFilesNames()) {
        bool flag{ false };

        if (ui->DeleteComboBox->currentText() == "ALL") {
            for (const auto& pair : this->Files) {
                for (const auto& value : pair.second) {
                    if (fs::remove(this->Path + value)) {
                        ui->Logs->append("- " + QString::fromStdString(value));
                    }
                }
            }

            ui->Logs->append("\nResult: All files have been successfully deleted.");
            flag = true;
        }

        for (const auto& pair : this->Files) {
            if (QString::fromStdString(pair.first) == ui->DeleteComboBox->currentText()) {
                for (const auto& value : pair.second) {
                    if (fs::remove(this->Path + value)) {
                        ui->Logs->append("- " + QString::fromStdString(value));
                    }
                }

                ui->Logs->append("\nResult: "
                                 + QString::number(pair.second.size()) + ' '
                                 + QString::fromStdString(pair.first)
                                 + " files have been successfully deleted.");

                flag = true;
                break;
            }
        }

        if (!flag) {
            this->Warning(ui->DeleteComboBox->currentText(), 1);
        }
    }
}
