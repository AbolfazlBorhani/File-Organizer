#ifndef FILEORGANIZER_H
#define FILEORGANIZER_H

#include <QMainWindow>
#include <QString>

#include <filesystem>
#include <vector>
#include <string>
#include <map>

#include <iostream>

typedef std::map<std::string, std::vector<std::string>> mvs;
typedef std::string str;

namespace fs = std::filesystem;

QT_BEGIN_NAMESPACE
namespace Ui { class FileOrganizer; }
QT_END_NAMESPACE

class FileOrganizer : public QMainWindow {
    Q_OBJECT
public:
    FileOrganizer(QWidget *parent = nullptr);
    ~FileOrganizer();

    str GetPath() const;
    bool ChackExistsDirectory(str&);
    void ClearAllVectors();
    bool SaveFilesNames();
    void Warning(QString, int);

private slots:
    void on_Show_clicked();

    void on_Categories_clicked();

    void on_Rename_clicked();

    void on_Delete_clicked();

private:
    Ui::FileOrganizer *ui;

    str Path{""};

    mvs Files{};
    // mvs TXT{};
    // mvs PNG{};
    // mvs JPG{};
    // mvs MP4{};
    // mvs MKV{};
    // mvs MOV{};
    // mvs MP3{};
    // mvs GIF{};
    // mvs WEBP{};
    // mvs WEBM{};
    // mvs HEIC{};
    // mvs ETC{};
};

#endif // FILEORGANIZER_H
