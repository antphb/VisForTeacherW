<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://upload.wikimedia.org/wikipedia/commons/b/bf/Logo_IUH.png" alt="Logo" width="100" height="50">
  </a>

  <h3 align="center">ĐỒ ÁN PHÁT TRIỂN ỨNG DỤNG</h3>

  <p align="center">
    Phát triển ứng dụng web giúp giáo viên chủ nhiệm theo dõi, quản lý, xem thống kê kết quả học tập của sinh viên.
    <br />
    <br />
    <a href="https://v4t.onrender.com/login/">View Demo</a>
    ·
    <a href="https://github.com/viCore12">Request Feature</a>
  </p>
</div>

![text](imageWeb/dangnhap.png)

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Nội dung</summary>
  <ol>
    <li>
      <a href="#about-the-project">Giới thiệu tổng quan</a>
      <ul>
        <li><a href="#built-with">Công nghệ sử dụng</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Kết quả đạt được</a>
      <ul>
        <li><a href="#prerequisites"></a>Giáo viên chủ nhiệm</li>
        <li><a href="#installation"></a>Quản trị viên</li>
      </ul>
    </li>
    <li><a href="#usage">Hiện thực</a></li>
    <li><a href="#roadmap">Hướng phát triển</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Giới thiệu tổng quan

Chào mừng bạn đến với ứng dụng web của chúng tôi - một công cụ hữu ích dành cho giáo viên chủ nhiệm để theo dõi, quản lý và xem thống kê kết quả học tập của sinh viên.

* Giao diện thân thiện với người dùng, thiết kế linh hoạt và dễ sử dụng.

* Trực hóa bằng nhiều biểu đồ, thống kê kết quả học tập đưa cái nhìn tổng quan về hiệu suất học tập của cá nhân và cả lớp học.


### Công nghệ sử dụng
1.	Ngôn ngữ lập trình:

- JavaScript: Ngôn ngữ phổ biến trong phát triển ứng dụng web.

- Python: Ngôn ngữ mạnh mẽ và linh hoạt, thích hợp cho phát triển web.

2.	Framework web:

- Django: Một framework Python mạnh mẽ để phát triển ứng dụng web.

- Rest framework: một toolkit mạnh mẽ và phổ biến để xây dựng các API Web bằng Django - một framework web Python cấp cao. Nó cung cấp các công cụ và tiện ích giúp dễ dàng xây dựng, kiểm thử và tài liệu hóa các API.

3.	Cơ sở dữ liệu:

- PostgreSQL: Hệ quản trị cơ sở dữ liệu phổ biến cho các ứng dụng web.

4.	Thư viện và công cụ phụ trợ:

- Apexchart.js: Một framework JavaScript dựa trên Vue.js để xây dựng các ứng dụng web và API.

- Plotly.js: Xây dựng và hiển thị các biểu đồ tương tác trong các ứng dụng web và API. Cung cấp một loạt các loại biểu đồ, bao gồm đường, cột, thanh, hình tròn, bánh, heatmap, scatter, box plot và nhiều hơn nữa.

- Chart.js: Thư viện JavaScript để tạo các biểu đồ và đồ thị tương tác.

- D3.js: Thư viện JavaScript mạnh mẽ để tạo và hiển thị dữ liệu trực quan.

5.	Xây dựng giao diện người dùng:

- HTML và CSS: Ngôn ngữ đánh dấu và kiểu định dạng phổ biến cho giao diện người dùng web.

- Bootstrap : Framework CSS phổ biến và thiết kế giao diện người dùng tiêu chuẩn.

* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![React][React.js]][React-url]

## Kết quả đạt được

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Giáo viên chủ nhiệm

- Đăng nhập: Giáo viên có thể đăng nhập vào hệ thống bằng tài khoản và mật khẩu được cung cấp.
- Xem thông tin cá nhân: Giáo viên có thể xem thông tin cá nhân đã được cung cấp trong hồ sơ.
- Cập nhật thông tin cá nhân: Giáo viên có thể cập nhật và chỉnh sửa thông tin cá nhân nếu có sự thay đổi.
- Xem thông tin điểm của sinh viên: Giáo viên có thể xem điểm của từng sinh viên trong lớp, bao gồm điểm số từng môn học và tổng kết.
- Ghi chú kết quả học tập và các thông tin quan trọng của sinh viên: Giáo viên có thể ghi chú các thông tin quan trọng về kết quả học tập của sinh viên, bao gồm lưu ý, đề nghị, phản hồi, hoặc những điểm cần cải thiện.
- Xem thống kê kết quả học tập của lớp: Giáo viên có thể xem thống kê tổng quan về kết quả học tập của toàn bộ lớp, bao gồm điểm trung bình, số lượng sinh viên đạt/không đạt, phân bố điểm, và các chỉ số thống kê khác.

### Quản trị viên

- Quản lý người dùng và phân quyền truy cập: Quản trị viên có quyền quản lý người dùng trong hệ thống, bao gồm tạo mới tài khoản giáo viên và sinh viên, cấp phép truy cập, và thiết lập phân quyền cho từng người dùng.
- Thêm, sửa đổi, xoá sinh viên trong lớp: Quản trị viên có thể thêm mới sinh viên vào lớp, sửa đổi thông tin sinh viên nếu cần thiết, và xoá sinh viên ra khỏi lớp học.
- Cập nhật điểm sinh viên: Quản trị viên có thể cập nhật điểm của sinh viên trong các môn học tương ứng.
- Đăng nhập: Quản trị viên có thể đăng nhập vào hệ thống bằng tài khoản và mật khẩu riêng.
- Xem thông tin cá nhân: Quản trị viên có thể xem thông tin cá nhân đã được cung cấp trong hồ sơ.
- Cập nhật thông tin cá nhân: Quản trị viên có thể cập nhật và chỉnh sửa thông tin cá nhân nếu có sự thay đổi.

<!-- CONTACT -->
## Contact
### Author 1
Your Name - [Nguyễn Thanh](https://www.facebook.com/NDThanh2011) - ngt2001@gmail.com

Kaggle Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)


### Author 2
Your Name - [Nhân Vi](https://www.facebook.com/nhan.vi.798) - nhanvi212@gmail.com

Kaggle Link: [https://www.kaggle.com/nhanvi](https://www.kaggle.com/nhanvi)

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
