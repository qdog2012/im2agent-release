import unittest

from update_release_readme import render_readme


class ReleaseReadmeTests(unittest.TestCase):
    version = "v2026.0915.1421"
    commit = "a" * 40
    intro = "# im2agent-release\n\nDownload the binaries here.\n"

    def notes(self, changes="- 新增处理进展\n- 修复设置同步"):
        return f"# im2agent {self.version}\n\n源代码提交：{self.commit}\n\n## 更新内容\n\n{changes}\n\n## 下载\n\n- Windows\n"

    def render(self, readme, notes=None):
        return render_readme(readme, notes or self.notes(), self.version, self.commit)

    def test_prepend_only_changes_and_preserve_intro(self):
        actual = self.render(self.intro)
        self.assertEqual(actual, f"## {self.version} 更新内容\n\n- 新增处理进展\n- 修复设置同步\n\n---\n\n{self.intro}")

    def test_same_release_retry_is_idempotent(self):
        actual = self.render(self.intro)
        self.assertEqual(self.render(actual), actual)

    def test_updated_notes_replace_same_version_and_keep_history(self):
        older = "## v2026.0909.1925 更新内容\n\n- 历史更新\n\n---\n\n"
        actual = self.render(older + self.intro)
        updated = self.render(actual, self.notes("- 更正说明"))
        self.assertEqual(updated.count(f"## {self.version} 更新内容"), 1)
        self.assertIn("- 更正说明", updated)
        self.assertNotIn("- 新增处理进展", updated)
        self.assertTrue(updated.endswith(older + self.intro))

    def test_older_release_cannot_displace_newer_release(self):
        with self.assertRaisesRegex(ValueError, "older release"):
            self.render("## v2026.0916.0001 更新内容\n\n- 新版\n\n" + self.intro)

    def test_missing_or_empty_changes_are_rejected(self):
        for notes in (self.notes(""), self.notes().replace("## 更新内容", "## 其他内容")):
            with self.subTest(notes=notes), self.assertRaises(ValueError):
                self.render(self.intro, notes)


if __name__ == "__main__":
    unittest.main()
